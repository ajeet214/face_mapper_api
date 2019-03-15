import os


class Config:

    DATABASE_CONFIG = {
        'host': os.environ.get('MONGO_HOST', 'localhost'),
        'port': os.environ.get('MONGO_PORT', 27017)
    }

    SELENIUM_CONFIG = {
        'host': os.environ.get('SELENIUM_HOST', 'localhost'),
        'port': str(os.environ.get('SELENIUM_PORT', 4444))
    }

    SOCIAL_SERVICES = {
        'facebook': {
            'host': os.environ.get('FACEBOOK_HOST', 'localhost'),
            'port': str(os.environ.get('FACEBOOK_PORT', 5001))
            },

        'twitter': {
            'host': os.environ.get('TWITTER_HOST', 'localhost'),
            'port': str(os.environ.get('TWITTER_PORT', 5002))
            },

        'linkedin': {
            'host': os.environ.get('LINKEDIN_HOST', 'localhost'),
            'port': str(os.environ.get('LINKEDIN_PORT', 5003))
            },

        'instagram': {
            'host': os.environ.get('INSTAGRAM_HOST', 'localhost'),
            'port': str(os.environ.get('INSTAGRAM_PORT', 5004))
            },

        'google-plus': {
            'host': os.environ.get('GOOGLE_PLUS_HOST', 'localhost'),
            'port': str(os.environ.get('GOOGLE_PLUS_PORT', 5006))
            }
        }

