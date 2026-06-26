---
title: "Why Use SecureKey Authentication?"
id: 4419723088791
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723088791-Why-Use-SecureKey-Authentication
updated_at: 2022-07-17T02:06:50Z
---

# Why Use SecureKey Authentication?

# Why Use SecureKey Authentication?

Logi SecureKey Authentication is provided for use in scenarios where a Logi application or Logi components are integrated with or embedded into a non-Logi application (the "Parent" application), which conducts the initial user authentication.

Sometimes called "single sign-on", this arrangement allows users to login once to the Parent application and yet have their security information propagated to other integrated applications, creating a seamless and secure user experience. This, of course, means that users can't be allowed to "go around" the Parent application and directly access the other applications. In the stateless world of web applications, this requires some special mechanisms to ensure security and they are
provided for Logi applications through our SecureKey technology.

The "authentication" part of SecureKey Authentication refers to the method used by the two applications to verify the validity of requests from users; this is a secondary authentication that occurs separately from the typical standard user login authentication.
