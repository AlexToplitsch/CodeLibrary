using System;
using System.Collections.Generic;
using System.Text;
using System.Globalization;

namespace ObserverPattern.Modules
{
    class Client : IObserver
    {
        private float Temp { get; set; }
        private float Moist { get; set; }
        private int Id { get; set; }
        private string WSName { get; set; }


        public Client(int id)
        {
            Id = id;
        }
        private void Display(string name, string timestamp)
        {
            Console.WriteLine($"Client: {Id} from: {name} at {timestamp}");
            Console.WriteLine($"Temp: {(int)Temp}°C");
            Console.WriteLine($"Moist: {(int)Moist}%");
            Console.WriteLine();
        }

        public void Update(WeatherStation item)
        {

                Temp = item.Temp;
                Moist = item.Moisture;
                Display(item.Name, item.Time);
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
