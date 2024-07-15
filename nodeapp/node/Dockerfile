# Base image
FROM node:16-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if using npm)
COPY package*.json .

# Install dependencies
RUN npm install

# Copy remaining application files (excluding node_modules)
COPY . .

# Build stage (optional, if using a build step)
# RUN npm run build  # Replace with your build command

# Switch to a slim runtime image
FROM node:16-alpine

WORKDIR /app

# Copy application files from builder stage
COPY --from=builder /app /app

# Expose port
EXPOSE 3000
# Or your chosen server port

# Start command
CMD [ "node", "index.js" ]
