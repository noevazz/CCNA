# HTTP

HTTP stands for Hypertext Transfer Protocol.

When you type a web address into your browser or click on a link, your browser sends an HTTP request to the server hosting that website, and the server responds with the requested data, typically in the form of a webpage.

## WWW

The "www" stands for World Wide Web. It is a system of interconnected hypertext documents accessed via the internet.

It was invented by **Sir Tim Berners-Lee** in 1989 and introduced to the public in 1991.

The World Wide Web is based on the use of hypertext, which allows users to navigate between web pages by clicking on hyperlinks. It's a way to access and share information across the internet using web browsers.

The "www" prefix is often used as part of website URLs (Uniform Resource Locators) to indicate that the address leads to a web page accessible via the World Wide Web.

The presence or absence of "www" in a URL can depend on how the website owner has configured their server and domain settings.

In the early days of the web, "www" was a commonly used subdomain prefix to indicate a web server. However, as the web evolved, it became more common for websites to function both with and without the "www" prefix, some websites prefer one version over the other for branding or technical reasons.

## HTTP Versions

- `HTTP/0.9`: This was the first version of HTTP, and it was very basic. It didn’t support headers or other features we associate with modern HTTP. It was introduced in the early 1990s.
- `HTTP/1.0`: Released in 1996, this version introduced several important features, including headers for request and response metadata and support for multiple media types. However, it still required a separate TCP connection for each resource, leading to performance issues.
- `HTTP/1.1`: Released in 1997, this version addressed some of the performance issues of HTTP/1.0 by introducing persistent connections (HTTP Keep-Alive), allowing multiple requests and responses to be sent over a single TCP connection. It also added features like chunked transfer encoding for efficient data transfer.
- `HTTP/2`: Introduced in 2015, HTTP/2 is a significant improvement over HTTP/1.1 in terms of performance. It uses a binary protocol and multiplexing, allowing multiple requests and responses to be sent in parallel over a single connection. It also includes features like header compression, server push, and stream prioritization.
- `HTTP/3`: HTTP/3, released in 2020, is the latest major version of the protocol. It is designed to improve performance and security further. HTTP/3 uses the **QUIC** (Quick UDP Internet Connections) transport protocol, which is built on top of UDP rather than TCP. It offers reduced latency and improved reliability.

Currently version 1.1 and 2 are widely used.

## How HTTP Works

HTTP works as a **request-response protocol** between a client (usually a web browser) and a server:

- `Client Request`: When you type a web address into your browser or click a link, the browser initiates an HTTP request to a server. This request includes a method (such as GET, POST, PUT, DELETE) that tells the server what action it wants to perform and the specific resource it's requesting.

- `Server Processing`: The server, upon receiving the request, processes it based on the method and the URL path specified. It then retrieves the requested resource, which could be a webpage, an image, a file, or any other type of data.

- `Server Response`: After processing the request, the server generates an HTTP response. This response includes a status code (indicating the success or failure of the request) and the requested resource. The response also contains headers providing additional information and metadata about the resource.

- `Client Display`: The client (web browser) receives the HTTP response. If the request was successful (status code 200 series), the browser renders the received resource, whether it's HTML content for a webpage, an image, or other media.

## HTTP Request Methods

Also know as "verbs" are actions that define what you want to do with a resource on the web. Here are some common ones:

- `GET`: Retrieve data from a specified resource. It's used for fetching information like web pages, images, files, etc. It's important to note that GET requests should not have any side effects on the server.

- `POST`: Submit data to be processed to a specified resource. This method is often used when you're submitting data to a server, like form submissions, file uploads, etc. It can create new resources or update existing ones.

- `PUT`: Uploads a representation of a resource or updates an existing resource at a specified URL. It replaces the entire resource if it exists or creates a new one if it doesn't.

- `DELETE`: Removes a specified resource. It deletes the resource identified by the URL.

GET, POST, PUT and DELETE are the most common methods, but there are still other ones:

- `PATCH`: Applies partial modifications to a resource. It's used to update part of a resource rather than replacing it entirely.

- `HEAD`: Similar to GET but only retrieves the headers of the response, not the actual content. It's often used to get meta-information about a resource without fetching the entire resource.

- `OPTIONS`: Requests information about the communication options available for a particular resource. It's used to check what HTTP methods and other options are supported for a resource.

- `TRACE`: Echoes back the received request to the client, which is primarily used for diagnostic purposes to see how a request changes as it passes through various proxies and servers.

These methods allow clients (like web browsers) to communicate with servers and perform various actions on resources over the web. Each method has its specific purpose and use case, contributing to the functionality and interactivity of web applications.

## Status Codes

HTTP status codes are standardized responses that web servers send to client requests to indicate the outcome of the request. They are three-digit numbers grouped into different categories:

- `1xx` - Informational: These codes indicate that the server has received the request and is continuing the process.

- `2xx` - Success: This category signifies that the request was received, understood, and processed successfully.

- `3xx` - Redirection: These codes indicate that further action needs to be taken to complete the request, such as redirection to another URL.

- `4xx` - Client Error: These codes are sent when there's an issue with the client's request, like requesting a resource that doesn't exist or lacking proper authentication.

- `5xx` - Server Error: This category signifies that the server failed to fulfill a valid request due to an error on the server side.

Some commonly encountered status codes include:

- 200 OK: The request has succeeded.
- 404 Not Found: The requested resource is not available on the server.
- 400 Bad Request: The server cannot process the request due to a client error, often due to malformed syntax.
- 500 Internal Server Error: A generic error message indicating that something has gone wrong on the server's end.

These status codes provide valuable information about the outcome of an HTTP request, aiding in troubleshooting and understanding the reason behind successes or failures in interactions between clients (like web browsers or apps) and servers.