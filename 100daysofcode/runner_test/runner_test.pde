
PImage far;
int bx = 0, bx2 = 600;
PImage back;
int mx = 0, mx2 = 600;
PImage fore;
int fx = 0, fx2 = 600;

void setup() {
    size(800, 600, P2D);

far = loadImage("far-buildings.png");
far.resize(800,600);
fore = loadImage("foreground.png");
fore.resize(800,600);
back = loadImage("back-buildings.png");
back.resize(800,600);
}

void draw() {
 fill(0,0,0);
  image(far,bx,0); image(far,bx,0);
image(back,mx,0); image(back,mx2,0);
image(fore,fx,0); image(fore,fx2,0);

  
  
bx-=0; bx2-=0;
mx-=1; mx2-=1;
fx-=2; fx2-=2;

if(bx<-600) {bx = 600;} if(bx2<-600) {bx2 = 600;}
if(mx<-600) {mx = 600;} if(mx2<-600) {mx2 = 600;}
if(fx<-600) {fx = 600;} if(fx2<-600) {fx2 = 600;}
}
