# Roadmap
---

## Introduction
This repository was created by cyber security enthusiasts as a collaborative knowledge base on various security related topics and to host the sources of a virtual environment built for practice and testing purposes. This document is therefore intended at providing an overview of the objectives of this project, as well as describing the standards adopted by its members.

## Objectives
As previously stated, the primary objective of this project is to provide an opportunity for members to practice on various security related topics. However, this essentially involves a the creation of a platform to configure, customise and deploy virtual machine on request. In the long term, this platform could be used for various types of security related exercises or challenges, such as CTF.

## Choice of topics
The project relies exclusively on the involvement of its members. Topics are suggested by members, and picked when a consensus is reached. Members should take the responsibility of contributing to project by proposing topics. For each topic, the idea is to propose a scenario in which a vulnerability is relevant, create a provisioning script and some instructions so that other members can practice. The provisioning script is later added to the environment so that it is possible to re-create an environment with the studied vulnerability later on. Members also have a certain ownerships of the topics they submit to the project. This means that if another member has a technical question about this specific topic, the author member should be able to provide some assistance. Likewise, members must create a wiki for each topic submitted. A template will be discussed later.

## Structure of the platform
Since _hackops_ is a collaborative project, the goal is to create a portable and flexible platform. This involves:
  1. The use of virtual machines. To increase cross-compatibility between OSs, the use of __Virtualbox__ as hypervisor is preferred
  * __Vagrant__ is used to manage the VMs' configuration and overall infrastructure of the environment
  * __Ansible__ is used to provision the VMs. It can easily be used with vagrant to provision VMs locally, and can later be used with cloud based providers such as Amazon
  * A custom Python (or other language, to be determined) randomisation program in charge of assigning playbooks to VMs in function of different users' inputs

Some important considerations:
  * Provisioning script should focus on one specific scripts. Several scripts can be assembled to provision a machine
  * Particular attention must be put on the development of the randomisation program to avoid generating unusable environments (unreachable or unexploitable VMs)
  * Provisioning scripts should specify OS versions (linux distributions in particular) if any platform specific code is part of the script
  * A system of tags to classify provisioning scripts should be created. This will allow for a certain level of customisation when generating environments. Such tag may include:
    * The level of complexity of the vulnerability
    * 1 to 3 keywords describing the content of the script
    * The name/version of OS/distribution
    * The author's username
