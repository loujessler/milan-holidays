from django_hosts import patterns, host
host_patterns = patterns('path.to',
    host(r'www', settings.ROOT_URLCONF, name='milan'),
    host(r'news', 'cz.urls', name='czech'),
)
