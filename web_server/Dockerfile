FROM nginx:latest

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy website files
COPY website/ /usr/share/nginx/html

# Set proper permissions
RUN chmod -R 755 /usr/share/nginx/html

# Expose HTTP & HTTPS ports
EXPOSE 80 443

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
