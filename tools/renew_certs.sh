#!/bin/bash

# Cert renew
#
# First install certbot:
# sudo apt-get update
# sudo apt-get install certbot
#
# Or update:
# sudo apt-get update
# sudo apt-get install --only-upgrade certbot
#
# Create a cert:
# sudo certbot certonly -d infinite-auto.ca -d www.infinite-auto.ca --manual
# sudo certbot certonly -d sandrako.ca -d www.sandrako.ca --manual
# sudo certbot certonly -d wojciklaw.ca -d www.wojciklaw.ca --manual
# sudo certbot certonly -d supersausage.ca -d www.supersausage.ca --manual
#
# Schedule renewal job every 2 months (cert has to be 30+ days old to renew):
# chmod +x renew_certs.sh
# sudo crontab -e
# 0 2 1 */2 * /var/web/wojciklaw.ca/tools/renew_certs.sh
#
# See logs:
# cat /var/log/letsencrypt/letsencrypt.log
#
# Cleanup old certs (if no longer renewing these) - otherwise error:
# certbot delete --cert-name infiniteauto.tech
#
# Renew all cmd:
# certbot renew --quiet

echo "$(date +"%Y-%m-%d %H:%M:%S") - Certificate renewal process started."


# Specify the base directory where SSL certificates are stored
BASE_CERT_DIR="/etc/letsencrypt/live/"

# List of certificate names
#CERT_NAMES=("infinite-auto.ca" "wojciklaw.ca" "sandrako.ca")
#CERT_NAMES=("infinite-auto.ca" )
# TODO: running this should do all (dont need loop below)
# TODO: test force:  certbot renew --quiet --force-renewal --debug  <- tihs is not working, manual need auth/challenge
# Renewal config file: /etc/letsencrypt/renewal/wojciklaw.ca.conf
certbot renew --quiet

## Iterate through each certificate and renew
#for CERT_NAME in "${CERT_NAMES[@]}"; do
#    CERT_DIR="$BASE_CERT_DIR/$CERT_NAME/"
#    echo "$(date +"%Y-%m-%d %H:%M:%S") - Renewing certificate: $CERT_NAME located at $CERT_DIR"
#
#    # Run Certbot to renew the certificates
#    certbot renew --quiet --deploy-hook "systemctl reload nginx" --cert-name "$CERT_NAME"
#
#    if [ $? -eq 0 ]; then
#        echo "$(date +"%Y-%m-%d %H:%M:%S") - Certificate renewal for $CERT_NAME successful. Restarting nginx..."
#        # Optional: Restart your web server or any other services using the renewed certificates
#        service nginx restart
#    else
#        echo "$(date +"%Y-%m-%d %H:%M:%S") - Certificate renewal for $CERT_NAME failed."
#    fi
#
#    echo "$(date +"%Y-%m-%d %H:%M:%S") - Certificate renewal process completed."
#done