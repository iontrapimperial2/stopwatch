#ifndef STOPWATCH_H
#define STOPWATCH_H

#include <QMainWindow>

namespace Ui {
class StopWatch;
}

class StopWatch : public QMainWindow
{
    Q_OBJECT

public:
    explicit StopWatch(QWidget *parent = nullptr);
    ~StopWatch();

private:
    Ui::StopWatch *ui;
};

#endif // STOPWATCH_H
