import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "TicTacToe"
SPRITE_SCALING_PLAYER = 3


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list_circle = None
        self.player_sprite_circle = None
        self.player_list_kreuz = None
        self.player_sprite_kreuz = None
        self.score_circle = 0
        self.score_kreuz = 0
        self.circle_number = 1
        self.kreuz_number = 1
        self.kreuz_winlist = []
        self.circle_winlist = []
        self.player_turn = 1

        #setmousevisibility
        self.set_mouse_visible(True)

        arcade.set_background_color(arcade.csscolor.WHITE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Sprite lists
        self.player_list_circle = arcade.SpriteList()
        self.player_list_kreuz = arcade.SpriteList()

        # Score
        self.score_circle = 0
        self.score_kreuz = 0
        self.circle_number = 1
        self.kreuz_number = 1

        # Character image from kenney.nl
        #kreis images
        self.player_sprite_circle1 = arcade.Sprite("circle1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_circle1.center_x = 50
        self.player_sprite_circle1.center_y = 50
        self.player_list_circle.append(self.player_sprite_circle1)
        
        self.player_sprite_circle2 = arcade.Sprite("circle2.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_circle2.center_x = 50
        self.player_sprite_circle2.center_y = 50
        self.player_list_circle.append(self.player_sprite_circle2)
        
        self.player_sprite_circle3 = arcade.Sprite("circle3.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_circle3.center_x = 50
        self.player_sprite_circle3.center_y = 50
        self.player_list_circle.append(self.player_sprite_circle3)
        
        self.player_sprite_circle4 = arcade.Sprite("circle4.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_circle4.center_x = 50
        self.player_sprite_circle4.center_y = 50
        self.player_list_circle.append(self.player_sprite_circle4)
        
        self.player_sprite_circle5 = arcade.Sprite("circle5.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_circle5.center_x = 50
        self.player_sprite_circle5.center_y = 50
        self.player_list_circle.append(self.player_sprite_circle5)
        
        #kreuz images
        self.player_sprite_kreuz1 = arcade.Sprite("cross1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_kreuz1.center_x = 100
        self.player_sprite_kreuz1.center_y = 100
        self.player_list_kreuz.append(self.player_sprite_kreuz1)
        
        self.player_sprite_kreuz2 = arcade.Sprite("cross2.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_kreuz2.center_x = 100
        self.player_sprite_kreuz2.center_y = 100
        self.player_list_kreuz.append(self.player_sprite_kreuz2)
        
        self.player_sprite_kreuz3 = arcade.Sprite("cross3.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_kreuz3.center_x = 100
        self.player_sprite_kreuz3.center_y = 100
        self.player_list_kreuz.append(self.player_sprite_kreuz3)
        
        self.player_sprite_kreuz4 = arcade.Sprite("cross4.png", SPRITE_SCALING_PLAYER)
        self.player_sprite_kreuz4.center_x = 100
        self.player_sprite_kreuz4.center_y = 100
        self.player_list_kreuz.append(self.player_sprite_kreuz4)
        #Set players turn
        self.player_turn = 1

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # define variables
        Grid_Frame_Color = arcade.color.BLACK
        # Code to draw the screen goes here
        arcade.draw_line(333,0,333,1000,Grid_Frame_Color,10)
        arcade.draw_line(666,0,666,1000,Grid_Frame_Color,10)
        arcade.draw_line(0,333,1000,333,Grid_Frame_Color,10)
        arcade.draw_line(0,666,1000,666,Grid_Frame_Color,10)

        self.player_list_circle.draw()
        self.player_list_kreuz.draw()



    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            if x < 333:
                if 999 > y > 666:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 166
                            self.player_sprite_circle1.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 166
                            self.player_sprite_circle2.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 166
                            self.player_sprite_circle3.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 166
                            self.player_sprite_circle4.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 166
                            self.player_sprite_circle5.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0

                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 166
                            self.player_sprite_kreuz1.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 166
                            self.player_sprite_kreuz2.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 166
                            self.player_sprite_kreuz3.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 166
                            self.player_sprite_kreuz4.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1

                if 666 > y > 333:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 166
                            self.player_sprite_circle1.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 166
                            self.player_sprite_circle2.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 166
                            self.player_sprite_circle3.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 166
                            self.player_sprite_circle4.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 166
                            self.player_sprite_circle5.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 166
                            self.player_sprite_kreuz1.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 166
                            self.player_sprite_kreuz2.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 166
                            self.player_sprite_kreuz3.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 166
                            self.player_sprite_kreuz4.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1

                if 333 > y > 0:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 166
                            self.player_sprite_circle1.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 166
                            self.player_sprite_circle2.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 166
                            self.player_sprite_circle3.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 166
                            self.player_sprite_circle4.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 166
                            self.player_sprite_circle5.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0

                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 166
                            self.player_sprite_kreuz1.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 166
                            self.player_sprite_kreuz2.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 166
                            self.player_sprite_kreuz3.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 166
                            self.player_sprite_kreuz4.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1


            if 333 < x < 666:
                if 999 > y > 666:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 499
                            self.player_sprite_circle1.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 499
                            self.player_sprite_circle2.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 499
                            self.player_sprite_circle3.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 499
                            self.player_sprite_circle4.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 499
                            self.player_sprite_circle5.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 499
                            self.player_sprite_kreuz1.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 499
                            self.player_sprite_kreuz2.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 499
                            self.player_sprite_kreuz3.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 499
                            self.player_sprite_kreuz4.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1

                if 666 > y > 333:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 499
                            self.player_sprite_circle1.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 499
                            self.player_sprite_circle2.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 499
                            self.player_sprite_circle3.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 499
                            self.player_sprite_circle4.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 499
                            self.player_sprite_circle5.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 499
                            self.player_sprite_kreuz1.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 499
                            self.player_sprite_kreuz2.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 499
                            self.player_sprite_kreuz3.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 499
                            self.player_sprite_kreuz4.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1

                if 333 > y > 0:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 499
                            self.player_sprite_circle1.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 499
                            self.player_sprite_circle2.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 499
                            self.player_sprite_circle3.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 499
                            self.player_sprite_circle4.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 499
                            self.player_sprite_circle5.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 499
                            self.player_sprite_kreuz1.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 499
                            self.player_sprite_kreuz2.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 499
                            self.player_sprite_kreuz3.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 499
                            self.player_sprite_kreuz4.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1

            if 666 < x < 999:
                if 999 > y > 666:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 832
                            self.player_sprite_circle1.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 832
                            self.player_sprite_circle2.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 832
                            self.player_sprite_circle3.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 832
                            self.player_sprite_circle4.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 832
                            self.player_sprite_circle5.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 832
                            self.player_sprite_kreuz1.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 832
                            self.player_sprite_kreuz2.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 832
                            self.player_sprite_kreuz3.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 832
                            self.player_sprite_kreuz4.center_y = 832
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1


                if 666 > y > 333:
                    if self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 832
                            self.player_sprite_circle1.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 832
                            self.player_sprite_circle2.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 832
                            self.player_sprite_circle3.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 832
                            self.player_sprite_circle4.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 832
                            self.player_sprite_circle5.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 832
                            self.player_sprite_kreuz1.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 832
                            self.player_sprite_kreuz2.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 832
                            self.player_sprite_kreuz3.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 832
                            self.player_sprite_kreuz4.center_y = 499
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1

                if 333 > y > 0:
                    if  self.player_turn == 1:
                        if self.circle_number == 1:
                            self.player_sprite_circle1.center_x = 832
                            self.player_sprite_circle1.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 2:
                            self.player_sprite_circle2.center_x = 832
                            self.player_sprite_circle2.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 3:
                            self.player_sprite_circle3.center_x = 832
                            self.player_sprite_circle3.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        elif self.circle_number == 4:
                            self.player_sprite_circle4.center_x = 832
                            self.player_sprite_circle4.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                        else:
                            self.player_sprite_circle5.center_x = 832
                            self.player_sprite_circle5.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "circle")
                            self.circle_number += 1
                            self.player_turn = 0
                    else:
                        if self.kreuz_number == 1:
                            self.player_sprite_kreuz1.center_x = 832
                            self.player_sprite_kreuz1.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 2:
                            self.player_sprite_kreuz2.center_x = 832
                            self.player_sprite_kreuz2.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        elif self.kreuz_number == 3:
                            self.player_sprite_kreuz3.center_x = 832
                            self.player_sprite_kreuz3.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1
                        else:
                            self.player_sprite_kreuz4.center_x = 832
                            self.player_sprite_kreuz4.center_y = 166
                            print("Left mouse button pressed at", x, y, "oberste Reihe links", "kreuz")
                            self.kreuz_number += 1
                            self.player_turn = 1


            elif button == arcade.MOUSE_BUTTON_RIGHT:
                print("Right mouse button pressed at", x, y)

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
