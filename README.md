# mltd-card-image-solver

A python based tool, used for merging cropped images.

## Usage

### Pre-processing

Place your target inside the `./images` folder, The program will use the folder to detect its type.  

Inside the `./images`, there will be two type options for selection, `Sprite` and `Texture2D`.

> The difference between `Sprite` and `Texture2D` is the former type is based on a varied image fragment, the program only needs to merge them, and the latter is a set of image fragments integrated into one image, The program must know where's the fragment range and rearrange them.

### Executing

Once placed, run the program and wait until `build` folder is generated.  

### Result

There will be the merged image inside the `build` folder.

## Example

The program contains example images for `Sprite` type, You can execute the program to see how's the result.

## Roadmap

- [ ] Add `argparse` functions  
- [ ] Add `Texture2D` type of method

## Issues

* `cv.imgshow()` 's second parameter cannot set with `cv.WINDOW_AUTOSIZE`

## Document references

* [合併圖片](https://blog.csdn.net/MDwalu/article/details/113774851)
* [預備知識](https://blog.csdn.net/Conyrol/article/details/96781786)

## License

Licensed under [MIT](LICENSE).

The copyright of any characters in the image belongs to [Bandai Namco Entertainment](https://www.bandainamcoent.co.jp/).  
