osc([81]).kaleid(2).color(0.3,0.5).rotate([40]).scale(14, 0.5, 8)
  .kaleid(24)
  .scrollY(0.5, 1.4)
  .mask(
    osc(512,({time}) => Math.sin(time/24) + 0.9 ) // offset
    .kaleid(3), [1,6], 0.5)// end mask
    .scrollX(1, 0.09)
    .scrollY(1, .333)
  .out(o1);
osc([14], [2]).rotate([1.4], [.04].fast(0.05), [7], [0.02].fast(20)).blend(o1, 7).out(o2);
osc(36).modulatePixelate(o1, 18).scrollX(0.3, [0.3, 3]).mult(o2, 256).mult(o1, -8).out(o0);
