-- file: fix-img-src.lua
function Image (img)
  print("before:" .. img.src)
  img.src = img.src:gsub("plots/", "")
  print("after:" .. img.src)
  return img
end