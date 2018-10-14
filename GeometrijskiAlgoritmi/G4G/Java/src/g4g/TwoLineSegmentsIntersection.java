package g4g;

/**
 * Created by dzimiks on 10/14/18.
 * <p>
 * https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
 */
public class TwoLineSegmentsIntersection {

    public static void main(String[] args) {
        Point p1 = new Point(1, 1);
        Point p2 = new Point(1, 2);
        Point q1 = new Point(10, 1);
        Point q2 = new Point(10, 2);

        System.out.println(p1);
        System.out.println(p2);
        System.out.println(q1);
        System.out.println(q2);
        System.out.println(doIntersect(p1, q1, p2, q2) ? "Yes\n" : "No\n");

        Point r1 = new Point(10, 0);
        Point r2 = new Point(0, 0);
        Point s1 = new Point(0, 10);
        Point s2 = new Point(10, 10);

        System.out.println(r1);
        System.out.println(r2);
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(doIntersect(r1, s1, r2, s2) ? "Yes" : "No");
    }

    private static boolean onSegment(Point p, Point q, Point r) {
        return (q.x <= Math.max(p.x, r.x) && q.x >= Math.min(p.x, r.x) &&
                q.y <= Math.max(p.y, r.y) && q.y >= Math.min(p.y, r.y));
    }

    private static int orientation(Point p, Point q, Point r) {
        float val = (q.y - p.y) * (r.x - q.x) -
                (q.x - p.x) * (r.y - q.y);

        if (val == 0) {
            return 0;
        }

        return val > 0 ? 1 : 2;
    }

    private static boolean doIntersect(Point p1, Point q1, Point p2, Point q2) {
        int o1 = orientation(p1, q1, p2);
        int o2 = orientation(p1, q1, q2);
        int o3 = orientation(p2, q2, p1);
        int o4 = orientation(p2, q2, q1);

        if (o1 != o2 && o3 != o4) {
            return true;
        }

        if (o1 == 0 && onSegment(p1, p2, q1)) {
            return true;
        }

        if (o2 == 0 && onSegment(p1, q2, q1)) {
            return true;
        }

        if (o3 == 0 && onSegment(p2, p1, q2)) {
            return true;
        }

        if (o4 == 0 && onSegment(p2, q1, q2)) {
            return true;
        }

        return false;
    }

    private static class Point {
        float x;
        float y;

        private Point(float x, float y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "Point{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }
}
