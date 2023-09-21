FROM python:3.9

RUN mkdir -p /opt/services/stripe-backend

WORKDIR /opt/services/stripe-backend

ADD . /opt/services/stripe-backend/

RUN chmod 755 /opt/services/stripe-backend/scripts/* && \
        chmod +x /opt/services/stripe-backend/scripts/* && \
            export DJANGO_SETTINGS_MODULE=stripe.settings && \
                pip install -r requirements.txt 