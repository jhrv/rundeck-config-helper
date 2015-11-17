import urllib2
import json

def main():
    fasitnodes = get_json("http://localhost:6969/fasit.json") 
    rundecknodes = map(to_rundeck_format, fasitnodes) 
    seraservers = get_json("http://localhost:6969/sera.json")
    for node in rundecknodes:
        for seraserver in seraservers:
            if node["nodename"] == seraserver["hostname"]:
                node["site"] = seraserver["site"]
    write_to_file(rundecknodes, "rundeck.json")

    
def write_to_file(dictionary, filename):
    jsonstring = json.dumps(dictionary, indent=4)
    f = open(filename, 'w')
    print >> f, jsonstring
    f.close()
    
def to_rundeck_format(node):
    return {"nodename": node['hostname']}

def get_json(url):
    payload = urllib2.urlopen(url).read()
    return json.loads(payload)


main()
