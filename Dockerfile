FROM node:20-bookworm
COPY app/app.js /app/app.js
WORKDIR /app
CMD ["node", "/app/app.js"]
