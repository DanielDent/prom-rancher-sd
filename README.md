# Prometheus-Rancher Service Discovery Bridge

This utility was created for [Cowhand](https://github.com/danieldent/cowhand).

prom-rancher-sd polls [Rancher's metadata service](http://docs.rancher.com/rancher/metadata-service/) and looks for containers with the `com.danieldent.cowhand.prom.port` label.

A configuration file suitable for use by [Prometheus](http://prometheus.io/) is written to enable services to be monitored automatically. Prometheus will scrape `/metrics` via HTTP by connecting to the container's primary IP on the port specified by the `com.danieldent.cowhand.prom.port` label.`

The [Let it Crash](http://c2.com/cgi/wiki?LetItCrash) design used implies that this software should be operated under a process supervisor. Docker and Rancher's automatic container restart facilities are believed adequate.

## License

Copyright 2016 [Daniel Dent](https://www.danieldent.com/).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use these files except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Third-party contents included in builds of the image are licensed separately.
