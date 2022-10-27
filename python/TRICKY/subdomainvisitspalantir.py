
import collections
input = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

def subDomainVisits(cpdomains):
    
    counts = collections.defaultdict(int)
        
    for domains in cpdomains:
        count, domains = domains.split()
        count = int(count)
        
        subdomain = domains.split(".")
        
        for i in range(len(subdomain)):
            counts[".".join(subdomain[i:])] += count
            
    return {f"{count} {domain}" for domain, count in counts.items()}

print(subDomainVisits(input))
            
            
