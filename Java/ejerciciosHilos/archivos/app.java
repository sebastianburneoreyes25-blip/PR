package ejerciciosHilos.archivos;

public class app {
        public static void main(String[] args) {
            DescargaImagenes img=new DescargaImagenes();
        DescargaVideos vid=new DescargaVideos();
        img.start();
        vid.start();
        }
}
