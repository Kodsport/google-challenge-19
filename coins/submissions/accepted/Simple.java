import java.awt.image.*;
import java.awt.*;
import javax.imageio.*;

public class Simple {

  public static void main(String... args) throws Exception {
    BufferedImage img = ImageIO.read(System.in);
    int nonwhite = 0;
    for (int i = 0; i < img.getWidth(); i++) {
      for (int j = 0; j < img.getHeight(); j++) {
        Color col = new Color(img.getRGB(i, j));
        if (col.getRed() + col.getBlue() + col.getGreen() < 255 + 255 + 255 - 20) {
          nonwhite++;
        }
      }
    }
    System.out.println(Math.round(nonwhite / 4180.0));
  }
}
