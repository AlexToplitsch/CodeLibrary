using ObserverPattern.Modules;
using System;
using System.Collections.Generic;

namespace ObserverPattern
{
    class Program
    {
        static void Main(string[] args)
        {
            WeatherStation graz = new WeatherStation("Graz");
            WeatherStation wien = new WeatherStation("Wien");
            WeatherStation tirol = new WeatherStation("Tirol");

            IObserver client1 = new ClientAverage(2);
            IObserver client = new Client(1);

            client1.Register(graz);
            client1.Register(wien);
            client.Register(graz);
            client.Register(tirol);
            client.Register(wien);

            graz.Run();
            tirol.Run();
            wien.Run();

            client1.Unregister(wien);
            client1.Register(tirol);

            graz.Run();
            tirol.Run();
            wien.Run();

        }
    }
}
