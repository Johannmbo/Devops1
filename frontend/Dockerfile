FROM nginx:alpine

# Удаляем стандартный конфиг nginx  
RUN rm /etc/nginx/conf.d/default.conf

# Копируем новый конфиг nginx  
COPY nginx.conf /etc/nginx/conf.d

# Копируем фронтенд файлы  
COPY index.html /usr/share/nginx/html/

EXPOSE 80