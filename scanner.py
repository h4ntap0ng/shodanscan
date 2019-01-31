import shodan
import sys

# Configuration
API_KEY = "YOUR_API_KEY"

# Input validation
if len(sys.argv) == 1:
        print 'Usage: %s <search query>' % sys.argv[0]
        sys.exit(1)

try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        query = ' '.join(sys.argv[1:])
        result = api.search(query)
        total = api.count(query, facets=FACETS)
         print 'Query: %s' % query
    print 'Total Results: %s\n' % result['total']
        # Loop through the matches and print each IP
        for service in result['matches']:
                print service['ip_str']
except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)
