import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    logging.info("Python app started. Running in Kubernetes pod...")
    try:
        while True:
            logging.info("App is still running...")
            time.sleep(36000)  # Sleep
    except KeyboardInterrupt:
        logging.info("Application stopped.")

if __name__ == "__main__":
    main()
