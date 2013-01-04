
public class test {

    static enum Edge {
        UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR
    }

    public static void main(String[] args) {

        Edge[] ep = { UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR };

        int s = 0;
        for (int i = 11; i >= 0 + 1; i--){
            for (int j = i - 1; j >= 0; j--){
                System.out.println(ep[j].ordinal() + " > " + ep[i].ordinal());
                if (ep[j].ordinal() > ep[i].ordinal()){
                    s++;
                }
            }
        }
    }
}
