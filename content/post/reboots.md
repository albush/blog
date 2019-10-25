+++
Date = "2014-09-30"
Title = "Minimizing the Impact of a Cloud Server Reboot"
+++

Last week at work, we had to reboot almost all of our Cloud servers. In anticipation of the reboots, my colleague Alison Oster and I wrote the following article for our customers. I think the advice is valid, regardless of where you host, so I'm reposting it here, and including the video hangout where we covered these tips.

<div class="video-container">
<iframe width="640" height="390" src="//www.youtube.com/embed/m9kg26vTGB0?list=UUG0VI_ayS-I0RQpBna4Tisw" frameborder="0" allowfullscreen></iframe></div>

# Minimizing the Impact of a Cloud Server Reboot

We all try to prevent it, but from time to time you might find that your server needs to be rebooted. While the reboot is generally a fast process, it can sometimes present additional headaches. Fortunately, a little bit of  planning can prevent a lot of headache. Let's go over a few tips to make sure that any server reboots are fast and minimally disruptive.

## Create a System Image for restoration and scaling

A system image is a snapshot of your server at a given point in time. You can use an image to build a replacement server, or to create redundancy and scalability.
Images are intended to capture the relatively static operating system, installed packages and configurations - not the dynamic data on the server. For Performance Cloud Servers only the System partition is imaged, which is why we recommend pairing system images with a Cloud Backup regimen.
System images can be taken ad hoc, or on a recurring scheduled basis. Recurring images are given a retention policy which saves new images for a fixed number of days before being replaced by the newest image. We recommend at least 3 days of images at any time.

For more information on Images see [this Rackspace guide to creating and restoring from images][1] and this [ Rackspace FAQ on scheduled images][2].


[14]: //www.rackspace.com/knowledge_center/article/cloud-essentials-creating-an-image-backup-cloning-and-restoring-a-server-from-a-saved-image
[15]: //www.rackspace.com/knowledge_center/article/scheduled-images-faq

## Ensure server has backups configured and running.

We recommend everyone use backups to keep their data up-to-date. The Rackspace Cloud Backup product runs a differential backup on a set frequency. This backup can be set to run on any number of directories. It is also important to remember that on Performance Cloud Servers with a data disc the data partition is not included in any image snapshots taken. Make sure those data partitions are included in your backup scheme.

For additional information on Cloud Backup, please review [the Rackspace Cloud Backup Overview in their Knowledge Center][1]:

   [1]: //www.rackspace.com/knowledge_center/article/rackspace-cloud-backup-overview



For many Linux servers these directories will need to be backed up:

* /home
* /root
* /etc (This will contain most of your configuration files)
* /var/www (This will often contain your websites and files)
* /var/lib/mysqlbackup (Servers built using Rackspace Managed Operations will have an automated process that automatically runs a mysql dump to this folder.)


For Windows Servers we recommend you backup where your data might be stored, e.g.:

* C:\inetpub
* C:\Users
* Any additional drives such D:, E: and so on.


#### MS-SQL Backup

Remember, Cloud Backup will not backup live databases. [Backup must be done through Microsoft SQL Server Management Studio][2].

   [2]: //www.rackspace.com/knowledge_center/article/backing-up-an-ms-sql-server-2008-database

 Of course we recommend that you carefully consider your specific applications, and their backup needs.

For additional reading, see: [notes on the differences between Cloud Backup and Image Snapshots.][3]

   [3]: //www.rackspace.com/knowledge_center/article/rackspace-cloud-backup-vs-cloud-server-image-backups


## Ensure services are configured to start after boot.

When installing a service it does not automatically configure this to start again once the server is rebooted.  However, there is an easy way to resolve this.  Below are some links on how to do this on RHEL/CentOS, Ubuntu and even Windows servers.

[How to use chkconfig with RHEL/CentOS][4]

   [4]: //www.rackspace.com/knowledge_center/article/centos-chkconfig

[How to use update-rc.d with Ubuntu][5]

   [5]: /products/f/25/t/4315

[Automatically Starting Services with Windows][6]

   [6]: //msdn.microsoft.com/en-us/library/windows/desktop/ms681957%28v=vs.85%29.aspx



**Ensure IPtables/Windows Firewall rules are saved and configured to restart on reboot.**

It is important to ensure that the firewall rules that you have worked hard to configure stay active upon reboot.  Below are a couple of links on how to ensure that this is the case for both [iptables][7] and [Windows Firewall.][8]

   [7]: https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s2-basic-firewall-activate-iptables.html
   [8]: //technet.microsoft.com/en-us/library/cc749262%28v=ws.10%29.aspx



**SSL passphrase**

We generally do not recommend using a passphrase when generating a SSL certificate.  If you do already have a passphrase in place for your SSL certificate however, you will need to input that into the server upon reboot.  The services on the server will not be able to start without first having to input that passphrase.



**Ensure that Cloud Block Storage Volumes Attach on Reboot**

If you have data on a Cloud Block Storage volume, you'll want to make sure that any volumes are properly connected after a reboot. To ensure this, you need to add your volume to the static file system information in the fstab file. See [step 5 in this guide][9].

   [9]: //www.rackspace.com/knowledge_center/article/prepare-your-cloud-block-storage-volume

For Windows users, mounted block storage should remain mounted after reboot.



**FSCK (File System Consistency Check)**

A [fsck][10] generally runs automatically at boot time.  There are 2 common triggers for automatically executing a fsck.  Either the operating system detect that a file system is in an inconsistent state (likely due to a non graceful shutdown like crash or power loss) or after a certain number of times that the system is mounted.

   [10]: /general/f/34/t/3756



Once you reboot your server this fsck may happen automatically.  If it does, this could cause an increase in the delay for your server coming back online.  Delay's are usually never good, but in this case the delay can save your server.  I would suggest just letting the fsck complete even though it may cause delays for you.  If you attempt to reboot the server again, it is just going to go right back into fsck which will only increase the delay.



## Test All The Things!

Having images, backups, configurations, and redundancies in place are vital, but we strongly recommend taking a few minutes to test the entire process of getting your environment back up and running, so that you know how your servers and other cloud products will react during and after the reboot. Want to know how your server will react to a reboot? There's no better way to get that answer than to just try it out and see. Of course we recommend doing any testing during the development phase, or on separate servers to limit any customer impact.



## Mitigating Reboot Impact



**Horizontal Scaling**

One of the best ways to prevent prolonged impact from a reboot is to distribute your application over multiple redundant, tiered, servers. We call this "Horizontal Scaling," and it's a great way to minimize the risk of downtime due to any single server going down. There's a very good [discussion of Horizontal Scaling][11] in one of the Rackspace Office Hours Hangouts I host.

   [11]: //www.rackspace.com/blog/examining-horizontal-scaling-google-hangout-recap/



**Custom Error Pages**

One benefit of using a Cloud Load Balancer is the ability to set a custom error page in the event that a server connected to the Load Balancer is offline or unresponsive. By proactively configuring that error page, a visitor to your site will receive an error message designed by you, specific to your unique application. Custom Error Pages can be configured via the [API][12] or the [Control Pane][13]l.

   [12]: //docs.rackspace.com/loadbalancers/api/v1.0/clb-devguide/content/Erropage-d1e666.html
   [13]: /products/f/25/t/3612
