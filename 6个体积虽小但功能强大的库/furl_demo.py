from furl import furl

f = furl('https://api.github.com/repos/psf/requests/issues')
f.args['per_page'] = 100

# Build whatever you want in any order
f.add({
    'state': 'open',
    'since': '2024-01-01T00:00:00Z',
    'labels': ['bug', 'enhancement'],   # stays as separate params
})

# Or chain fluently
f.set({
    'state': 'closed',
    'sort': 'created',
    'direction': 'desc'
}).remove(['since'])        # drop a param easily

# Add your token as fragment (common pattern for SPAs)
f.fragment.path = 'access_token'
f.fragment.args['token'] = 'ghp_supersecrettoken123'
f.fragment.args['expires'] = 3600

print(f.url)