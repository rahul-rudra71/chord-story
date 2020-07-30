class PlayerSprite(pygame.sprite.Sprite):

    def __init__(self):
        super(PlayerSprite, self).__init__()

        # create image array
        self._images = []
        
        self._images.append(pygame.image.load("assets/images/player1.png").convert())
        self._images.append(pygame.image.load("assets/images/player2.png").convert())

        # index to get image
        self._index = 0

        # image displayed is the image at the current index
        self._image = self._images[self._index]
        self._image.set_colorkey((255, 255, 255))

        # initial player rect
        self._rect = pygame.Rect(215, 200, 30, 36)


    def update(self):
        # reset index when reach end
        if self._index >= len(self._images):
            self._index = 0

        # update image to display
        self._image = self._images[self._index]
        self._image.set_colorkey((255, 255, 255))

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, images):
        self._images = images

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self._index = index

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect