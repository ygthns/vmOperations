# Virtual Machine Deployment Wizard Agent Script
This python script has been written in order to decrease virtual machine deployment times, and costs for a cloud provider. Code developed for being used as agent scripts in client instances, which means this codes need to be placed inside of the virtual machine image, and triggered by crontab in every 30 seconds. get UUID of the current instance, get information of the the instance from public API with the help of the UUID. If it detects any changes, then it applies changes.
### What Changes?
1. Storage size.
2. Hostname changes.
3. Password changes.

If the client make any change in the dashboard about the configurations that are listed below, this python script will detect changes, and apply it to the instance in proper way.
Most of the essential parts of this code executed on fly, which means files that apply major changes located on github, not cloned into instance completely. Cloned into ram, executed and removed.

```
url_repo='https://raw.githubusercontent.com/ygthns/vmOperations/main/plusclouds.automation.python.script.storage/{}/storage.py'.format(distroName)
response_url = urllib.request.urlopen(url_repo)
data_url = response_url.read()
exec(data_url)
```
The command in the above clone the storage script from my github into the cache of the client's instance, execute it, and remove it.

### Benefits of this approach
1. Maintanence of the code for the future. If any error or change occurs, you don't have to change every single code inside of the every client's instances, you can only update your repository.
2. You don't need to reveal your code to your client anymore. Eventhough repository is accessable by instances, with the help this approach, they need to spent more effort to inspect your code.
