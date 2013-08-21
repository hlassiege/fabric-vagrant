# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
	config.vm.box = "precise32"
	config.vm.box_url = "http://files.vagrantup.com/precise32.box"
	#config.vm.network :private_network, ip: "192.168.50.4"

	config.vm.synced_folder 'C:\Users\hugo\vagrant\apt\cache', "/var/cache/apt/archives" 
	config.vm.synced_folder 'C:\Users\hugo\vagrant\gems\1.8', "/opt/vagrant_ruby/lib/ruby/gems/1.8"
	config.vm.synced_folder 'C:\Users\hugo\vagrant\tmp', "/vagrant/tmp"
  
	config.vm.provision :fabric do |fab|
		fab.tasks = ["java es_install"]
	end  	

end
