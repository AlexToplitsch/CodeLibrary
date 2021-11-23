using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern.Modules
{
    class ClientAverage : IObserver
    {

        private float Temp { get; set; }
        private float Moist { get; set; }
        private Dictionary<string, List<float>> Temps { get; set; } = new Dictionary<string, List<float>>();
        private Dictionary<string, List<float>> Moists { get; set; } = new Dictionary<string, List<float>>();
        private int Id { get; set; }
        private string WSName { get; set; }

        public ClientAverage(int id)
        {
            Id = id;
        }
        private void Display(string name, string time)
        {

            Console.WriteLine($"Client: {Id} from: {name} at {time}");
            Console.WriteLine($"Actual Temp in: {(int)Temp}°C");
            Console.WriteLine($"Actual Moist: {(int)Moist}%");
            Console.WriteLine($"Average Temp: {(int)CalcAverageTemp()}°C");
            Console.WriteLine($"Average Moist: {(int)CalcAverageMoist()}%");
            foreach (var item in Temps)
            {
                Console.Write($"{(int)item}, ");  
            }
            Console.WriteLine();
            foreach (var item in Moists)
            {
                Console.Write($"{(int)item}, ");
            }
            Console.WriteLine();
            Console.WriteLine();
        }

        public void Update(WeatherStation item)
        {
            if(WSName != item.Name)
            {
                Moists.Clear();
                Temps.Clear();
            }
            WSName = item.Name;
            Temp = item.Temp;
            Moist = item.Moisture;
            Moists.Add(Moist);
            Temps.Add(Temp);
            Display(item.Name, item.Time);

        }

        private float CalcAverageMoist()
        {
            float sum = 0;
            foreach(float moist in Moists)
            {
                sum += moist;
            }
            return sum / Moists.Count;
        }

        private float CalcAverageTemp()
        {
            float sum = 0;
            foreach (float moist in Temps)
            {
                sum += moist;
            }
            return sum / Temps.Count;
        }

        public void Register(WeatherStation ws)
        {
            ws.Register(this);
        }
        public void Unregister(WeatherStation ws)
        {
            ws.Unregister(this);
        }
    }
}
