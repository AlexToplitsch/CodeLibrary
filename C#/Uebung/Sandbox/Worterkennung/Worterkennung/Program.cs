using System;

namespace Worterkennung
{
    class Program
    {
        static void Main(string[] args)
        {
            string satz = Console.ReadLine();
            int anzahl_woerter = 1;
            int index = 0;

            for(int i = 0; i < satz.Length; i++)
            { 
                if(satz[i] == ' ')
                {
                    anzahl_woerter++;
                }
            }
            Console.WriteLine("Es befinden sich " + anzahl_woerter + " Wöter in diesem Satz!");

            string[] woerter = new string[anzahl_woerter];

            for(int i = 0; i  < anzahl_woerter; i++)
            {
                string wort = "";

                for(int j = 0; j < satz.Length; j++)
                {
                    if(index >= satz.Length)
                    {
                        break;
                    }
                        wort = wort + satz[index];

                    if(satz[index] == ' ' || satz[index] =='.' || satz[index] == '?' || satz[index] == '!')
                    {
                        index++;
                        break;
                    }
                    
                    index++;
                }
                woerter[i] = wort;
                Console.WriteLine(woerter[i]);
            }

        }
    }
}
