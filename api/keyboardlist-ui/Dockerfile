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

ENTRYPOINT ["./bin/build.sh"]
