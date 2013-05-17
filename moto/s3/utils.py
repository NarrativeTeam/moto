import re
import urllib2
import urlparse

bucket_name_regex = re.compile("(.+).s3.amazonaws.com")


def bucket_name_from_url(url):
    domain = urlparse.urlparse(url).netloc

    # If 'www' prefixed, strip it.
    domain = domain.lstrip("www.")

    if 'amazonaws.com' in domain:
        bucket_result = bucket_name_regex.search(domain)
        if bucket_result:
            return bucket_result.groups()[0]
    else:
        if '.' in domain:
            return domain.split(".")[0]
        else:
            # No subdomain found.
            return None

def key_name_from_url(url):
    key_name = urlparse.urlparse(url).path.lstrip('/')
    return key_name


def clean_key_name(key_name):
    return urllib2.unquote(key_name)
