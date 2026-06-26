---
title: "Data Playback and Live Mode"
id: 4405851125143
section: "Introduction to  Logi Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851125143-Data-Playback-and-Live-Mode
updated_at: 2021-09-21T01:29:13Z
---

# Data Playback and Live Mode

# Data Playback and Live Mode

There is one common attribute to all data streams: ​time.​ Any data source that has a date-time field can be playable in the Composer time bar (Data DVR). Historical data can be played back visually, just like replaying a movie. Data sources that host frequently updated data can be configured to play data in live mode. In live mode, Composer uses internal markers to automatically push incremental updates to visuals. Live mode updates are configurable from as frequently as once a second, to once a minute, hour, or day.

You do not need to force expensive full query refreshes, and since only newly arrived data is pushed to your visuals, network and other resources are conserved. Composer's built-in live mode functionality increases productivity and overall user satisfaction when working with very large and rapidly updated data.

Like Data Sharpening, the time bar streams data to the user over WebSocket connections. Within your WebSocket connection, Composer multiplexes commands from each visual over that connection so each visual's query request results in its own virtual communication channel that receives data streaming in one direction, and sends control commands, such as changing playback speed, pausing, or flipping the time window in the other direction.

For more information, see [*Live Mode and Historical Playback*](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback).
