// Requirements
var gulp = require('gulp'),
    $ = require('gulp-load-plugins')(),
    path = require('path'),
    merge = require('merge-stream');

// Pull environment variables
var dist_dir = process.env.DIST_DIR || './dist';
var work_dir = process.env.WORKDIR || '.';

// Our front-end apps, relative to work_dir (only one for now)
var app_dir = path.join(work_dir, 'app');
var config = path.join(app_dir, 'gulp_config.json');
var files = require(path.resolve(config));

// Vendor files
var vendors = ['angular', 'angular-route', 'uikit'];
var vendor_dist = path.resolve(path.join(app_dir, 'lib'));

// ============================================================================
// Build JS
// ============================================================================
gulp.task('build-js', function() {
  var streams = [];

  // Build JS file for item defined inside gulp_config.json
  Object.keys(files.src.js).forEach(function(key) {
    var src = files.src.js[key].map(function(value) {
      return path.join(app_dir, value);
    });
    var dist = key;
    var stream = gulp.src(src)
      .pipe($.sourcemaps.init())
      .pipe($.concat(dist))
        // Only rename and uglify if gulp is ran with --type production
        // .pipe($.util.env.type == 'production' ? $.rename({suffix: ".min"}) : $util.noop())
        // .pipe($.util.env.type == 'production' ? $.uglify() : $util.noop())
      .pipe($.sourcemaps.write())
      .pipe(gulp.dest(dist_dir));
    streams.push(stream);
  });

  // Return the merged streams
  return merge.apply(null, streams);
});

// ============================================================================
// Build CSS
// ============================================================================
gulp.task('build-css', function() {
  var streams = [];

  Object.keys(files.src.less).forEach(function(key) {
    var src = files.src.less[key].map(function(value) {
      return path.join(app_dir, value);
    });
    var dist = key;
    var stream = gulp.src(src)
      .pipe($.sourcemaps.init())
      .pipe($.less())
      .pipe($.sourcemaps.write())
      .pipe(gulp.dest(dist_dir));
    streams.push(stream);
  });

  // Return the merged streams
  return merge.apply(null, streams);
});

// ============================================================================
// Copy vendor files
// ============================================================================
gulp.task('copy-vendor', function() {
  var vendor_files = vendors.map(function(vendor) {
    return path.join('node_modules', vendor, '**/*.*');
  });
  gulp.src(vendor_files, { base: './node_modules'})
    .pipe(gulp.dest(vendor_dist));
});

// ============================================================================
// Watch
// ============================================================================
gulp.task('watch', function() {
  var js = app_dir + '**/*.js';
  var less = app_dir + '**/*.less';
  gulp.watch([js], ['build-js']);
  gulp.watch([less], ['build-css']);
});


gulp.task('default', ['copy-vendor', 'build-js', 'build-css']);
gulp.task('dev', ['default', 'watch']);
