String genre;
int index;

void setup()
{
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
}
void loop()
{
    genre = "pop";
    String genreList[] = {"hip-hop", "pop", "country", "jazz+"};
    
    for(int i = 0; i < sizeof(genreList) / sizeof(genreList[0]); i++) {
        if(genreList[i] == genre) {
            digitalWrite(i, HIGH);
        }
        else {
            digitalWrite(i, LOW);
        }
    }
}