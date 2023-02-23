# Extending Elastic Beanstalk Linux platforms


## Platform hooks

Platform hooks are specifically designed to extend your environment's platform. These are custom scripts and other executable files that you deploy as part of your application's source code, and Elastic Beanstalk runs during various instance provisioning stages.

- Note: Platform hooks aren't supported on Amazon Linux AMI platform versions (preceding Amazon Linux 2).


### Application deployment platform hooks

An application deployment occurs when you provide a new source bundle for deployment, or when you make a configuration change that requires termination and recreation of all environment instances.

To provide platform hooks that run during an application deployment, place the files under the .platform/hooks directory in your source bundle, in one of the following subdirectories.

- __prebuild__/: Files here run after the Elastic Beanstalk platform engine downloads and extracts the application source bundle, and before it sets up and configures the application and web server.
  - The `prebuild` files run after running commands found in the commands section of any configuration file and before running Buildfile commands.

- __predeploy__/: Files here run after the Elastic Beanstalk platform engine sets up and configures the application and web server, and before it deploys them to their final runtime location.
  - The `predeploy` files run after running commands found in the container_commands section of any configuration file and before running Procfile commands.

- __postdeploy__/: Files here run after the Elastic Beanstalk platform engine deploys the application and proxy server.
  - This is the last deployment workflow step.
