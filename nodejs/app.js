var express = require('express'),
    path = require('path'),
    fs = require('fs'),
    formidable = require('formidable'),
    readChunk = require('read-chunk'),
    readChunk = require('serve-static'),
    fileType = require('file-type');

var app = express();

app.set('port', (process.env.PORT || 80));

// Tell express to serve static files from the following directories
//app.use(express.static('public'));
//app.use('/uploads', express.static('uploads'));

// Tell express to serve static files from the following directories
app.use(express.static('public'));
//app.use('/data/uploads', express.static('/data/uploads'));
app.use(serve-static('/data'));
app.use('data', serve-static('/data'));



/**
 * Index route
 */
app.get('/', function (req, res) {
    // Don't bother about this :)
    var filesPath = path.join(__dirname, 'uploads/');
    fs.readdir(filesPath, function (err, files) {
        if (err) {
            console.log(err);
            return;
        }

        files.forEach(function (file) {
            fs.stat(filesPath + file, function (err, stats) {
                if (err) {
                    console.log(err);
                    return;
                }

                var createdAt = Date.parse(stats.ctime),
                    days = Math.round((Date.now() - createdAt) / (1000*60*60*24));

                if (days > 1) {
                    fs.unlink(filesPath + file,(err) => { if (err) throw err; console.log('Rename complete!');});
                }
            });
        });
    });

    res.sendFile(path.join(__dirname, 'views/index.html'));
});

/**
 * Upload photos route.
 */
app.post('/upload_photos', function (req, res) {
    var photos = [],
        form = new formidable.IncomingForm();

    // Tells formidable that there will be multiple files sent.
    form.multiples = true;
    // Upload directory for the images
    form.uploadDir = path.join(__dirname, 'tmp_uploads');

    // Invoked when a file has finished uploading.
    form.on('file', function (name, file) {
        // Allow only 3 files to be uploaded.
        if (photos.length === 3) {
            fs.unlink(file.path);
            return true;
        }

        var buffer = null,
            type = null,
            filename = '';

        buffer = readChunk.sync(file.path, 0, 262);
        type = fileType(buffer);

        // Check the file type, must be either png,jpg or jpeg
        if (type !== null && (type.ext === 'png' || type.ext === 'jpg' || type.ext === 'jpeg')) {
            // Assign new file name
            filename = Date.now() + '-' + file.name;

            // Move the file with the new file name
            //fs.rename(file.path, path.join(__dirname, 'uploads/' + filename),(err) => { if (err) throw err; console.log('Rename complete!');});
            // Move the file with the new file name
            fs.copyFile(file.path, path.join('/data', filename),(err) => { if (err) throw err; console.log('Rename complete!');});

            var vid = builder.create('picture');
            vid.att('priority','1')
            vid.att('time_played','0')
            vid.ele('filename', '/data/'+filename );
            vid.ele('duration', '15' );
            vid.ele('schedule',  '*/1 * * * *');
            
            var xmldoc = vid.toString({ pretty: true });
            fs.writeFile('/data/'+filename+'.xml', xmldoc, function(err) {if(err) { return console.log(err); }});

            // Add to the list of photos
            photos.push({
                status: true,
                filename: filename,
                type: type.ext,
                publicPath: '/' + filename
            });
        } else {
            photos.push({
                status: false,
                filename: file.name,
                message: 'Invalid file type'
            });
            fs.unlink(file.path,(err) => { if (err) throw err; console.log('Rename complete!');});
        }
    });

    form.on('error', function(err) {
        console.log('Error occurred during processing - ' + err);
    });

    // Invoked when all the fields have been processed.
    form.on('end', function() {
        console.log('All the request fields have been processed.');
    });

    // Parse the incoming form fields.
    form.parse(req, function (err, fields, files) {
        res.status(200).json(photos);
    });
});

app.listen(app.get('port'), function() {
    console.log('Express started at port ' + app.get('port'));
});
