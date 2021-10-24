#!/usr/bin/lua

for line in io.lines() do
   local pinyin, word, feq = string.match(line, "^(.+),(.+),(%d*)$")
   if pinyin ~= nil and word ~= nil then
      io.write(string.format("%s %s\n", word, string.gsub(pinyin, "-", "'")))
   end
end
