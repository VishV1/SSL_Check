Usage:

      Build: docker build  -t  <image_name>  .
      RUN: docker run <Image_name> <domain_name>

1. How would you scale this script and run it with resiliency to e.g. handle 1000s of domains?**
   
    To scale the script for thousands of domains, we can use multi-threading for parallel processing or leverage distributed computing with technologies like Docker or AWS Lambda. By loading domain names into a queue, multiple processes can efficiently handle them, ensuring scalability and resilience

2. How would you monitor/alert on this service?
   
   we have to monitor the infrastrucre such as CPU, memory and Network I/O and also the application part by tracking the number of failed scans, scan durations and system logs for errors and warnings. Alerting can be done by using the rules based on thresholds on the metrics    or the logs. Alerts can be sent out by any monitoring tool such as Datadog or Splunk.
   
3. What would you do to handle adding new domains to scan or certificate expiry events from your service?

    we can maintain the config file or DB with the all the domain names, any new domains can be added to this which will be picked by the script while scanning. we can load them to queue and take advantage of the distributed comupting scalability and resilience.
    we can update the script to look for the cert expiry and send alerts if they are nearing expiry like in 2 months
    
4. After some time, your report requires more enhancements requested by the Tech team of the company. How would you handle these "continuous" requirement changes in a sustainable manner?

    To handle continuous requirement changes in a sustainable manner, We have to maintain proper version control and branching, develop a        thorough automated testing process, and set up continuous integration and continuous delivery pipelines
