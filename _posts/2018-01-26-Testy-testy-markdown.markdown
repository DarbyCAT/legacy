---
layout: post
title: "Testy testy markdown"
date: 2018-01-26 17:46:44 -0500
categories: testing markdown
author: testuser
filename: /files/
---
# Structured documents

Sometimes it's useful to have different levels of headings to structure your documents. Start lines with a `#` to create headings. Multiple `##` in a row denote smaller heading sizes.

### This is a third-tier heading

You can use one `#` all the way up to `######` six for different heading sizes.

If you'd like to quote someone, use the > character before the line:

> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway

### MathJax test:

<span>\\(x = {-b \pm \sqrt{b^2-4ac} \over 2a}\\)</span>

Hi jaco

This is some inline <span>\\(\sum\limits_{x=0}^{4} x\\)</span> for loops yea

<pre class="prettyprint linenums:1">
local lwGetMode     = _G.love.window.getMode
local lgPush        = _G.love.graphics.push
local lgPop         = _G.love.graphics.pop
local lgTranslate   = _G.love.graphics.translate
local lgScale       = _G.love.graphics.scale
local lgRectangle   = _G.love.graphics.rectangle
local lgSetColor    = _G.love.graphics.setColor
local lmGetPosition = _G.love.mouse.getPosition
local min = math.min
 
local TLfres = {}
 
local lastMouseX, lastMouseY = 0, 0
local currentlyRendering
 
-- Internal helper function
local function _getRawMousePosition(width, height)
   local x, y = lmGetPosition()
   local w, h = lwGetMode()
   local scale = min(w/width, h/height)
   return (x - (w - width * scale) * 0.5)/scale, (y - (h - height * scale) * 0.5)/scale
end
 
-- Use this any time you would normally call love.mouse.getPosition.
-- The returned position is scaled to the given dimensions.
function TLfres.getMousePosition(width, height)
   local x, y = _getRawMousePosition(width, height)
   if x >= 0 and x <= width and y >= 0 and y <= height then
      lastMouseX, lastMouseY = _getRawMousePosition(width, height)
   end
   return lastMouseX, lastMouseY
end
 
-- Calculate the current scale based on the desired dimensions and current ones
-- If called within a rendering block, width and height are optional.
function TLfres.getScale(width, height)
   if currentlyRendering then
      width  = width  or currentlyRendering[1]
      height = height or currentlyRendering[2]
   end
   local w, h = lwGetMode()
   return min(w/width, h/height)
end
 
-- Zooms and centers to fit width×height into the current window.
-- 0,0 is at the top-left of the canvas, or the middle if centered is true.
-- Use love.graphics.push before this and love.graphics.pop after done rendering
function TLfres.beginRendering(width, height, centered)
   if currentlyRendering then
      error("Must call tlfres.endRendering before calling beginRendering.")
      return
   end
   currentlyRendering = {width, height}
   lgPush()
 
   local w, h = lwGetMode()
   local scale = min(w/width, h/height)
   lgTranslate((w - width * scale) * 0.5, (h - height * scale) * 0.5)
   lgScale(scale)
   if centered then
      lgTranslate(0.5 * width, 0.5 * height)
   end
   return scale
end
 
local _black = {0, 0, 0, 255}

-- Pops out of the transform; if letterboxColor is true, draws black letterbox
-- bars. letterboxColor can also be any {r, g, b, a} table.
function TLfres.endRendering(letterboxColor)
   if not currentlyRendering then
      error("Must call tlfres.beginRendering before calling endRendering.")
      return
   end
   local width, height = currentlyRendering[1], currentlyRendering[2]
   currentlyRendering = nil
   lgPop()
 
   local w, h = lwGetMode()
   local scale = min(w/width, h/height)
   width, height = width * scale, height * scale
 
   lgSetColor(letterboxColor or _black)
   lgRectangle("fill", 0, 0,  w,  0.5 * (h - height)) -- top
   lgRectangle("fill", 0, h,  w, -0.5 * (h - height)) -- bottom
   lgRectangle("fill", 0, 0,  0.5 * (w - width), h)   -- left
   lgRectangle("fill", w, 0, -0.5 * (w - width), h)   -- right
end
 
return TLfres
</pre>