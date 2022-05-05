[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://user-images.githubusercontent.com/552629/76405509-87025300-6388-11ea-86c9-af882abb00bd.png" width="80" height="80" />
  <img src="README_IMGS/Amazon_Web_Services_Logo.png" alt="Logo" width="100" height="80">

  <h3 align="center">Simple Serverless MiddleWare in AWS with Edge-Computing </h3>

  <p align="center">
    This project is one niddleware to build simple serveless application with edge-computing concept executing one little database in SQLite in the client browser. 
    <br />
    <br />
    <a href="http://cqs-sales.s3-website.eu-central-1.amazonaws.com/">Demo</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#installation">Usage</a></li>
      </ul>
    </li>
    <li><a href="#AWS-architecture">AWS Architecture</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The project contain one website connected to s3 to download the necessary database to show the sales. The files download from the S3 are .db file (little file with databases in SQLite). These file are load in the SQLite wasm in the client side.

The clients process the database in the browser to show the data and add the new bids and send them to AWS to send through the websockets to other clients using one API-gateway Websocket.

So in this project there are:
* Hosting Static web in S3
* The web reads from S3 bucket the database.db file
* SQLite executions in the client side
* SQLite file modification (UPDATES/INSERTS) using python and save it in S3
* Websocket connecitons with API-gateway 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- BUILT STARTED -->
### Built With

This section list the frameworks/libraries used to create this blog. 

* [S3 AWS](https://aws.amazon.com/es/s3/)
* [Lambda AWS](https://aws.amazon.com/es/lambda/)
* [SQS AWS](https://aws.amazon.com/es/sqs/)
* [API-gateway](https://aws.amazon.com/es/api-gateway/)
* [JavaScript](https://www.javascript.com/)
* [SQLite](https://sql.js.org/)
* [Python](https://www.python.org/)
* [Boto3](https://aws.amazon.com/es/sdk-for-python/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

In this section I explain you about how you can import this project to your AWS account to test it.This code can be used in your project to manage the websocket conections. 

You can select what technology you will use to manage the connections. You can use S3 or SQS to manage the connections denepnds of these election you have to import the [S3-connectionManagement](https://github.com/eduardfores/CQS_Sale/tree/main/AWS-lambda/S3-connectionManagment) or [SQS-connectionManagement](https://github.com/eduardfores/CQS_Sale/tree/main/AWS-lambda/SQS-connectionManagment).

```diff
- AWS S3 is more expensive but is more fast
- AWS SQS is more cheap but is more slow
```

### Prerequisites

This is an example of how to install the functions you need to use the software and how to install them.

* S3 configuration

You have to configure S3 with static host endpoint 
[Hosting Static in AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

<p style="color: red"> All files in this bucket must be PUBLIC </p>

```diff
+ You have to configure S3 or SQS depending what tecnology you want to use to manage the connections.
```
* SQS configuration

You must create a standard queue in SQS service
[Create queue in AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html)

<p style="color: red"> You can create a FIFO queue but for this project is not necessary </p>

* S3 configuration

You must upload the empty file [connections.config](https://github.com/eduardfores/CQS_Sale/blob/main/connections.config) in S3.

```diff
- !!! connections.config never has to be PUBLIC !!!
```

### Installation

_Below is the instructions to install the application in AWS Step by step or how to use the files in your project as middleware._

#### To Test

1. You have to import to you S3 all files and directories of my gitHub in public ACL. You must add [connections.config](https://github.com/eduardfores/CQS_Sale/blob/main/connections.config) only when you are using the S3 connection managment with SQS method is not necessary. The AWS-lambda directory is not necessary

2. You have to create one API-gateway with websockets with endpoints Connection, Disconnect and sendMessage.

3. You have to import the CQSSales-connect lambda in the Connection endpoint.

4. You have to import the CQSSales-disconnect in the Disconnect endpoint.

5. You have to import the CQSSales-managment in the sendMessage endpoint.

_With these imports you can test my demo web_

#### To Use as Middleware

1. You have to import [websocket-client.js](https://github.com/eduardfores/CQS_Sale/blob/main/js/webSocket/webSocket-client.js) to your web or application.

2. You have to create one API-gateway with websockets with endpoints Connection, Disconnect and sendMessage.

3. You have to import the CQSSales-connect lambda in the Connection endpoint.

4. You have to import the CQSSales-disconnect in the Disconnect endpoint.

5. You have to import the CQSSales-managment in the sendMessage endpoint.

<p align="right">(<a href="#top">back to top</a>)</p>

## AWS Architecture

_The Architecture can be expressed with the next diagram_

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/eduardfores/CQS_Weather/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/eduard-for%C3%A9s-ferrer-354b61163/