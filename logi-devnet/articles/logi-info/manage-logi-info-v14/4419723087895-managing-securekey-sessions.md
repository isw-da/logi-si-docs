---
title: "Managing SecureKey Sessions"
id: 4419723087895
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723087895-Managing-SecureKey-Sessions
updated_at: 2022-07-17T02:06:50Z
---

# Managing SecureKey Sessions

# Managing SecureKey Sessions

This topic introduces ways to manage your SecureKey sessions.

## Application Server Time-out Configuration

Automatic **session****time-out** after a period of inactivity is managed in the web server and, for example, the IIS default setting is 20 minutes. You may want to adjust this to a shorter interval in order to increase session security, which is done in a variety of ways. For example, for IIS, this is set in IIS Manager tool or in the web.config or machine.config
files; for Tomcat, it's set in the web.xml file. While this, by itself, is not completely secure (it still presents a window of opportunity
until the time-out occurs), it's a good practice
that helps minimize security exposure.

## Session Exit Elements

The **Action.Exit** and **Response.Exit** elements immediately end the current session and redirect the browser to a URL. In Logi Info, you can initiate this from your parent application by browsing directly to a process task in the Logi app, which runs Response.Exit. Otherwise, both actions are usually initiated by a user action, such as clicking a "Logout" button or link (however, user behavior in this regard may not always be reliable).

## Restart Session Attribute

The Security element's **Restart Session** attribute causes previous session information to be cleared with each new SecureKey authentication attempt. Turning this feature on is the recommended method of ensuring that users do not "piggyback" onto a previous user's session.

This requires, however, that your parent application be designed correctly: the authentication routine in the parent app *always* needs to include a Logi SecureKey authentication request. It should not, for example, include code that tests to see if a Logi session exists and then skips issuing a new SecureKey request if it does. Ensuring that there's a new SecureKey request with each report request will guarantee that other sessions that are not valid (such as those created by using browser bookmarks
or
shared links)
will be rejected and redirected back to the parent app for authentication. It will also ensure
that different users on the same machine/browser will also have to authenticate
properly (providing that the original user logs out of the parent application session).
