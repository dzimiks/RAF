package g4g;

import javafx.util.Pair;

import java.util.Collections;
import java.util.Comparator;
import java.util.Vector;

/**
 * Created by dzimiks on 10/14/18.
 * <p>
 * https://www.geekforgeeks.org/klees-algorithm-length-union-segments-line/
 */
public class KleesAlgorithm {

    public static void main(String[] args) {
        Vector<Pair<Integer, Integer>> segments = new Vector<>();
        segments.add(new Pair<>(3, 15));
        segments.add(new Pair<>(2, 5));
        segments.add(new Pair<>(4, 8));
        segments.add(new Pair<>(9, 12));

        System.out.println("Segments: " + segments);
        System.out.println("Length of Union of all segments: " + segmentUnionLength(segments));
    }

    // O(nlogn)
    private static int segmentUnionLength(Vector<Pair<Integer, Integer>> seg) {
        int n = seg.size();
        int result = 0;
        int cnt = 0;
        Vector<Pair<Integer, Boolean>> points = new Vector<>(n * 2);

        for (Pair<Integer, Integer> val : seg) {
            points.add(new Pair<>(val.getKey(), false));
            points.add(new Pair<>(val.getValue(), true));
        }

//        for (int i = 0; i < n; i++) {
//            points.add(new Pair<>(seg.get(i).getKey(), false));
//            points.add(new Pair<>(seg.get(i).getValue(), true));
//        }

        // Lambda sort
        Collections.sort(points, (p1, p2) -> Integer.compare(p1.getKey(), p2.getKey()));

//        Collections.sort(points, new Comparator<Pair<Integer, Boolean>>() {
//            @Override
//            public int compare(Pair<Integer, Boolean> p1, Pair<Integer, Boolean> p2) {
//                return Integer.compare(p1.getKey(), p2.getKey());
//            }
//        });

        System.out.println("Points:   " + points);

        for (int i = 0; i < n * 2; i++) {
            if (cnt > 0) {
                result += points.get(i).getKey() - points.get(i - 1).getKey();
            }

            if (points.get(i).getValue()) {
                cnt--;
            } else {
                cnt++;
            }
        }

        return result;
    }
}
