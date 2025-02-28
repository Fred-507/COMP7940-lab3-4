import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read configuration file
config.read('config.ini')

print (config['TELEGRAM']['ACCESS_TOKEN'])