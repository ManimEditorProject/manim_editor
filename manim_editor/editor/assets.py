import os
from manim import VGroup, SVGMobject, ORIGIN, RIGHT, UP, LEFT, WHITE, DEGREES, DOWN, PI, MathTex, Tex, TexFontTemplates
from manim.mobject.geometry import ArrowTriangleFilledTip, Triangle, Square, Circle, Rectangle, Sector, RoundedRectangle
from .config import get_config


class IconNormal(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        icon_normal = SVGMobject(os.path.join(get_config().STATIC_DIR, "img", "play_btn.svg"))
        self.add(icon_normal)


class IconSkip(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        icon_skip = SVGMobject(os.path.join(get_config().STATIC_DIR, "img", "wind.svg"))
        self.add(icon_skip)


class IconLoop(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        icon_loop = SVGMobject(os.path.join(get_config().STATIC_DIR, "img", "arrow_clockwise.svg"))
        self.add(icon_loop)


class IconCompleteLoop(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        icon_completeloop = SVGMobject(os.path.join(get_config().STATIC_DIR, "img", "hourglass_split.svg"))
        self.add(icon_completeloop)

class EditorLogo(VGroup):
    def __init__(self):
        VGroup.__init__(self)
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        triangle = Triangle(color=logo_red, fill_opacity=1,z_index=10).shift(1.2*RIGHT)
        square = Square(color=logo_blue, fill_opacity=1,z_index=20).shift(UP)
        circle = Circle(color=logo_green, fill_opacity=1,z_index=30).shift(LEFT)
        logo = VGroup(triangle, square, circle).scale(2.5)
        logo.move_to(ORIGIN)
        self.add(logo)
        
        l1 = Rectangle(height=1.7, width=0.6, stroke_width=0, fill_opacity=1,z_index=11)
        l2 = l1.copy()
        pause = VGroup(l1,l2).arrange(RIGHT)
        pause.move_to(triangle.get_center_of_mass())
        self.add(pause)
        
        play= Triangle(color=WHITE, fill_opacity=1,z_index=21).rotate(-90*DEGREES).move_to(square.get_center()).scale(1.5).shift(0.2*RIGHT)
        self.add(play)
        
        inner=1.2
        outer=1.75
        arc= Sector(arc_center=circle.get_center(), inner_radius=inner,outer_radius=outer, start_angle=-PI/2, angle=-1.5*PI,color= WHITE, stroke_width=0, z_index=31)
        tip = ArrowTriangleFilledTip(z_index=31,color=WHITE,start_angle=-PI/2).scale(3.5)
        tip.next_to(arc.get_right(), DOWN,buff=0).shift((outer-inner)/2*LEFT+0.05*UP)

        loop = VGroup(arc,tip).rotate(-PI/16)
        self.add(loop)   


class EditorBanner(VGroup):
    def __init__(self):
        VGroup.__init__(self)
      
        logo_all= EditorLogo().scale(0.5)

        logo_black = "#343434"
        M = MathTex(r"\mathbb{M}").scale(7).set_color(logo_black)
        anim= Tex(r"\textbf{anim}",tex_template=TexFontTemplates.gnu_freeserif_freesans).scale(7).set_color(logo_black).scale(0.75748)

        E = MathTex(r"\mathbb{E}").scale(7).set_color(logo_black)
        ditor= Tex(r"\textbf{ditor}",tex_template=TexFontTemplates.gnu_freeserif_freesans).scale(7).set_color(logo_black).scale(0.75748)
        x=VGroup(M,anim).arrange(RIGHT, buff=0.1)
        y=VGroup(E,ditor).arrange(RIGHT,buff=0.1)
        banner=VGroup(x,y,logo_all).arrange(RIGHT,buff=0.5)
        anim.align_to(M,DOWN)
        ditor.align_to(M,DOWN)
        self.add(RoundedRectangle(fill_color="#ece6e2",height=banner.get_height()+1, width=banner.get_width()+1.5,fill_opacity=1, stroke_width=0, z_index=0))
        self.add(banner)
        self.scale(0.3)