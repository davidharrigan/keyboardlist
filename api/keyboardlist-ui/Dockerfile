FROM node

# Set some envvars
ENV WORKDIR /usr/src/app
ENV DIST_DIR /usr/src/app/dist

# Create our workdir
RUN mkdir -p $WORKDIR
WORKDIR $WORKDIR

# Copy files and install deps
COPY . ./
RUN npm install
RUN node_modules/gulp/bin/gulp.js
