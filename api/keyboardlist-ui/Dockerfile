FROM node

# Set some envvars
ENV DIST_DIR /dist
ENV WORKDIR /usr/src/app

# Create our workdir
RUN mkdir -p $WORKDIR
WORKDIR $WORKDIR

# Copy files and install deps
COPY . ./
RUN npm install

ENTRYPOINT ["./bin/build.sh"]
