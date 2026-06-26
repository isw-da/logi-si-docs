---
title: "Logi Info - How to Embed Video"
id: 360048644474
section: "Samples"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048644474-Logi-Info-How-to-Embed-Video
updated_at: 2022-02-07T21:45:36Z
---

# Logi Info - How to Embed Video

### Question:

How do you embed a video into a report definition?

### Answer:

Currently, there is no native video element within Logi Info Studio.  
  
However, you can use an Include Html element to place your video into a report definition as you would any normal website. For example, using the HTML5 Video script provided by w3schools and the Big Buck Bunny video; the following is an example.

```
<video width="400" controls>  
 <source src="https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4" type="video/mp4">  
 <source src="https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_stereo.ogg" type="video/ogg">  
 Your browser does not support HTML5 video.  
</video>  
  
<p>  
Video courtesy of   
<a href="https://www.bigbuckbunny.org/" target="_blank">Big Buck Bunny</a>.  
</p>
```

### Further Reading

w3schools source: [Click Here](https://www.w3schools.com/html/html5_video.asp)

Big Buck Bunny source: [Click Here](https://peach.blender.org/download)

IncludeHTML element: [Click Here](https://devnet.logianalytics.com/hc/en-us/articles/4419722951831-Insert-HTML-into-Reports)
